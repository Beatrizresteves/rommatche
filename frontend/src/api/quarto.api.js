import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  getQuartos: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/quartos/list_quartos")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  addNewQuarto: (data) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/quartos/add_quarto", apiHelpers.dataToForm({ data }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
}
