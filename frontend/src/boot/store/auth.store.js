import { apolloService } from '@plugins/apollo'
import JwtService from '@services/jwt.service'
import gql from 'graphql-tag'

const apollo = apolloService.defaultClient

const state = {
  errors: [],
  user: 'Anonymous User',
  isAuthenticated: !!JwtService.getToken(),
  authenting: false
}

const getters = {
  currentUser (state) { return state.user.replace(`${process.env.ORGANIZATION}__`, '') },
  isAuthenticated (state) { return state.isAuthenticated },
  errors (state) { return state.errors },
  authenting (state) {
    return state.authenting
  }
}

const actions = {
  login (context, credentials) {
    context.commit('setAuthenting', true)
    return apollo
      .mutate({
        mutation: gql`
          mutation {
            kerberosAuth (
              username:"${credentials.username}"
              password:"${credentials.password}"
            )
            {
              token
              payload
            }
          }
        `
      }).then(({ data }) => {
        context.commit('setAuth', data.kerberosAuth)
      }).catch((error) => {
        context.commit('setErrors', error)
      })
  },
  verifyAuth (context) {
    const token = JwtService.getToken()
    if (!token) return 0
    apollo
      .mutate({
        mutation: gql`
          mutation {
            verifyToken(token:"${token}")
            {
              payload
            }
          }
        `
      }).then(({ data }) => {
        context.commit('setAuth', data.verifyToken)
      })
      .catch(() => {
        context.commit('purgeAuth')
      })
  },
  logout (context) {
    context.commit('purgeAuth')
  }
}

const mutations = {
  setAuthenting (state) {
    state.authenting = true
  },
  setAuth (state, token) {
    state.isAuthenticated = true
    state.user = token.payload.username
    if ('token' in token) JwtService.saveToken(token)
    state.authenting = false
  },
  setErrors (state, error) {
    state.errors = [error]
    state.authenting = false
  },
  purgeAuth (state) {
    state.authenting = false
    state.isAuthenticated = false
    state.user = 'Anonymous User'
    state.errors = []
    JwtService.destroyToken()
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}
