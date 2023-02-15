<template>
  <div>
    <v-btn
      v-if="loggedUser"
      color="black"
      min-width="140"
      height="40px"
      rel="noopener noreferrer"
      size="x-large"
      variant="flat"
      :to="{ name: 'accounts-login' }"
      rounded
      class="my-4">
      <v-img width="30px" class="mr-2" src="@/assets/icone.png"/>
      Likesadd
    </v-btn>
    <v-row align="center" class="text-center">
      <!-- <v-col cols="6">
        <v-select
          label="Selecione uma cidade"
          :items="cityslist"
          prepend-icon="mdi-map"
        ></v-select>
      </v-col> -->
      <v-col cols="12" sm="6" offset-sm="3">
        <v-select
          label="Selecione uma cidade"
          :items="cityslist"
          prepend-icon="mdi-map"
        ></v-select>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import {debouncerdecorator} from '@/debouncer.js'
  // import {requests} from '@/apimock/requests.js'
  import AccountsApi from "@/api/accounts.api.js"
  export default {
    data () {
      return {
      states: ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceara", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "	Paraná", "Pernambuco", "Piauí"],
      citys: [],
      stateSelect: "",
      statessearch: null,
      stateslist: [],
      cityslist: ["Belo Horizonte", "São José dos Campos", "São Paulo", "Rio de Janeiro", "Montes Claros"],
    
    watch: {
      statessearch () {
        this.procuraEstados
      },
    },
    methods: {
      procuraEstados: debouncerdecorator(async function () {
        let myself = await AccountsApi.whoami()
        console.log(myself)
        // this.statesloading = true
        // const data = await requests.search_citys(this.statessearch)
        // this.stateslist = data.cidades
        // this.statesloading = false
      }, 500),
      async listaCidades(){
        // this.citysloading = true
        // const data = await requests.search_citys(this.states)
        // this.cityslist = data
        // this.citysloading = false
      },
      // statesA() {
      //   this.states = this.cityslist.?.[nome]
      //   }
      select() {
        this.stateSelect = this.state.title
        this.citys = this.cityslist.stateSelect
        }
      }
    }
  }
}
</script>