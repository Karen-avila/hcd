import { apolloService } from '@/core/services/apollo.service'
import JwtService from '@/core/services/jwt.service'
import gql from 'graphql-tag'

const apollo = apolloService.defaultClient

const state = {
  errors: [],
  user: 'Anonymous User',
  isAuthenticated: !!JwtService.getToken()
}

const getters = {
  currentUser (state) { return state.user },
  isAuthenticated (state) { return state.isAuthenticated },
  errors (state) { return state.errors }
}

const actions = {
  login (context, credentials) {
    return apollo
      .mutate({
        mutation: gql`
          mutation {
            tokenAuth (
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
        context.commit('setAuth', data.tokenAuth)
      }).catch((error) => {
        context.commit('setErrors', error)
      })
  },
  verifyAuth (context) {
    const token = JwtService.getToken()
    if (!token) return 0
    apollo
      .query({
        query: gql`
          query {
            verifyToken(token:"${token}")
            {
              payload
            }
          }
        `
      }).then(({ data }) => {
        context.commit('setAuth', data.verifyToken)
      })
      // .then((data) => {
      // console.log('setUser0: ', data.payload.username)
      // apollo.subscribe({ query: this.$gql` subscription { hello } ` })
      //   .subscribe({
      //     next (data) { console.log(data) },
      //     error (error) { console.error(error) }
      //   })
      // })
      .catch(() => {
        context.commit('purgeAuth')
      })
  },
  logout (context) {
    context.commit('purgeAuth')
  }
}

const mutations = {
  setAuth (state, token) {
    state.isAuthenticated = true
    state.user = token.payload.username
    if ('token' in token) JwtService.saveToken(token)
  },
  setErrors (state, error) {
    state.errors = [error]
  },
  purgeAuth (state) {
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
