<template>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <template #progress>
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title>{{ title }}</v-card-title>

    <v-card-text>
      <div class="my-4 text-subtitle-1">
        $ {{ value }}
      </div>

      <div>{{ description }}</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>{{ items }}</v-card-title>

     <div>
      <v-btn
        class="ma-2"
        text
        icon
        color="#5DCAD1"
      >
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>

      <v-btn
        class="ma-2"
        text
        icon
        color="primary"
      >
        <v-icon>mdi-thumb-down</v-icon>
      </v-btn>
    </div>
    <p class="ma-2"> {{ items.nome }}</p>
    <p class="ma-2"> {{ items.valor }}</p>
    {{ items.description }}
      <maths :quartos="item"/>
         <!-- <v-col v-for="item in items" :key="item.id" cols="12">
        <task :quarto="item" />
      </v-col> -->
  </v-card>
 
</template>
<script>
import { useAppStore } from "@/stores/appStore"
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import QuartosApi from "@/api/quarto.api.js"
import Maths from './Maths.vue'

  export default {
  components: { Maths },
    setup() {
      const appStore = useAppStore()
      return { appStore }
    },
    data: () => ({
      loading: false,
      selection: 1,
      title: "mmksmkf",
      value: "1220",
      name: "José",
      description: "fnkdnfkjsnkjnskjfnskjfnksjnfkjsfkjsnfkjsn",
      items: [],
    }),
    computed: {
      ...mapState(useAccountsStore, ["loggedUser"]),
    },
    mounted() {
      this.getQuartos()
    },
    methods: {
      getQuartos() {
        this.loading = true
        QuartosApi.getQuartos().then((data) => {
          this.items = data
          this.loading = false
        })
      },
      addNewQuarto(quarto) {
        this.loading = true
        QuartosApi.addNewQuarto(quarto.name).then((quarto) => {
          this.appStore.showSnackbar(`Novo quarto adicionada #${quarto.id}`)
          this.getQuartos()
          this.loading = false
          console.log("oi")
        })
      },
    },
  }
</script>