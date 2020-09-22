import gql from 'graphql-tag'

export const GET_TOKEN = (credentials) => {
  return gql`
  mutation {
    tokenAuth (
      username: "${credentials.username}"
      password: "${credentials.password}"
      )
      {
        token
        payload
        refreshExpiresIn
        coreuser {
          id
          username
          visibleUsername
          getAllPermissions
          organization {
            id
            name
            code
            sites {
              domain
            }
            modules {
              name
            }
          }
        }
      }
    }
    `
}

export const VERIFY_TOKEN = (token, user) => {
  return gql`
  query {
    verifyToken( token: "${token}" )
    {
      payload
    }
    coreuser( id: "${user}" ) {
      id
      username
      visibleUsername
      getAllPermissions
      organization {
        id
        name
        code
        sites {
          domain
        }
        modules {
          name
        }
      }
    }
  }
  `
}
