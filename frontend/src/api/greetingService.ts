import { createApi } from "./ApiFactory"

const greetingApi = createApi("http://127.0.0.1:5000")
const defaultHeaders = {
  Accept: "application/json",
  "Content-Type": "application/json;charset=UTF-8",
}
export const greetingService = {
  getDefaultGreeting: async function () {
    const { data } = await greetingApi.request({
      url: `/greeting`,
      method: "GET",
      headers: defaultHeaders
    })
    return { greeting: data.greeting }
  },
  
  getMongoGreeting: async function () {
    const { data } = await greetingApi.request({
      url: `/greeting/mongo`,
      method: "GET",
      headers: defaultHeaders
    })
    return { greeting: data.greeting }
  }
}