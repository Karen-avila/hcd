import VueApollo from 'vue-apollo'
import { ApolloClient } from 'apollo-client'
import { createHttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { split } from 'apollo-link'
import { WebSocketLink } from 'apollo-link-ws'
import { getMainDefinition } from 'apollo-utilities'
import JwtService from '@services/jwt.service'

const GRAPHQL_URL = process.env.APOLLOHTTP
const GRAPHQLWS_URL = process.env.APOLLOWS

const getHeaders = () => {
  const headers = {
    authorization: ''
  }
  headers.authorization = `JWT ${JwtService.getToken()}`
  return headers
}

const httpLink = createHttpLink({
  uri: GRAPHQL_URL,
  fetch,
  headers: getHeaders()
})

const wsLink = new WebSocketLink({
  uri: GRAPHQLWS_URL,
  headers: getHeaders(),
  options: {
    reconnect: true
  }
})

const link = split(
  ({ query }) => {
    const definition = getMainDefinition(query)
    return definition.kind === 'OperationDefinition' &&
      definition.operation === 'subscription'
  },
  wsLink,
  httpLink
)

const apolloClient = new ApolloClient({
  link: link,
  cache: new InMemoryCache(),
  connectToDevTools: true
})

export const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})
