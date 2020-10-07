
export const getToken = () => {
  return window.localStorage.getItem('userToken')
}

export const saveToken = token => {
  window.localStorage.setItem('userToken', token.token)
}

export const destroyToken = () => {
  window.localStorage.removeItem('userToken')
}

export default { getToken, saveToken, destroyToken }
