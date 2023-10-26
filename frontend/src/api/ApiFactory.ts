import axios, { AxiosInstance } from "axios"

const defaultErrorHandler = (error) => {
  const statusCode = error.response?.status

  // logging only errors that are not 401
  if (statusCode && statusCode !== 401) {
    console.error(error)
  }
  return Promise.reject(error)
}

export const createApi = (baseURL: string, errorHandler?: any): AxiosInstance => {
  const api = axios.create({
    baseURL: baseURL,
  })
  const err = (errorHandler) ? errorHandler : defaultErrorHandler
  api.interceptors.response.use(undefined, (error) => {
    return err(error)
  })
  return api
}