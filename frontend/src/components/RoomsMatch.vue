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

    <v-card-title>{{ name }}</v-card-title>

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
      <!-- <v-col v-for="item in items" :key="item.id" cols="12">
        <task :quarto="item" />
      </v-col> -->
    </div>
  </v-card>
 
</template>
<script>
import { useAppStore } from "@/stores/appStore"
import QuartosApi from "@/api/quartos.api.js"

  export default {
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
    mounted() {
      this.getQuartos()
    },
    methods: {
      getQuartos() {
        this.loading = true
        QuartosApi.getQuartos().then((data) => {
          this.items = data.quartos
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