/* eslint-disable no-undef */
export const requests = {
    search_citys(){
        // const url = `https://api.github.com/search/users?q=${searchstring}`
        // const response = await fetch(url)
        // return await response.json()
        const url = require("@/apimock/server/data/citys.json")
        return url
	}
}