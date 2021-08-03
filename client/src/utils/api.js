import axios from 'axios'
import qs from 'qs'

const instance = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? '' : 'http://127.0.0.1:5000',
  timeout: 10000
})

const get = function (api, params) {
  return new Promise((resolve, reject) => {
    instance({
      url: api,
      method: 'GET',
      params: params
    }).then(res => {
      resolve(res)
    }).catch(err => {
      reject(err)
    })
  })
} // server: request.args

const post = function (api, data) {
  return new Promise((resolve, reject) => {
    instance({
      url: api,
      method: 'POST',
      data: qs.stringify(data),
      dataType: 'text',
      headers: {
        'content-type': 'application/x-www-form-urlencoded'
      }
    }).then(res => {
      resolve(res)
    }).catch(err => {
      reject(err)
    })
  })
} // server: request.form

// const post = function (api, data) {
//   return new Promise((resolve, reject) => {
//     instance({
//       url: api,
//       method: 'POST',
//       data: data,
//       dataType: 'json',
//       headers: {
//         'content-type': 'application/json'
//       }
//     }).then(res => {
//       resolve(res)
//     }).catch(err => {
//       reject(err)
//     })
//   })
// } // server: request.json

export {
  get,
  post
}
