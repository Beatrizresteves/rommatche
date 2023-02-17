<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <!-- <v-col cols="12">
        <task-form :form-label="'Nova Tarefa'" @new-task="addNewTask" />
      </v-col> -->
        <!-- <v-autocomplete
          label="Autocomplete"
          :items="cidades"
        ></v-autocomplete> -->
      <v-col v-for="item of items" :key="item.id" cols="auto" width="1000" :class="['d-flex justify-center align-center', `elevation-${n}`]">
          <v-card
            :loading="loading"
            class="mx-auto my-12"
            width="350"

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
              :src="item.imagem"
            ></v-img>

            <v-card-title>{{ item.nome }}</v-card-title>

            <v-card-text>
              <div class="my-4 text-subtitle-1">
                $ {{ item.valor }}
              </div>

              <div>{{ item.description }}</div>
            </v-card-text>

            <v-divider class="mx-4"></v-divider>

            <v-card-title>{{ item.cidade }}</v-card-title>


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
          </v-card>
      </v-col>
    </v-row>
  </v-container>

 
</template>
<script>
import { useAppStore } from "@/stores/appStore"
import QuartosApi from "@/api/quarto.api.js"

export default {
  props: ['cidadeEscolhida'],
  setup() {
      const appStore = useAppStore()
      return { appStore }
    },
    data() {
      return {
        loading: false,
        // selection: 1,
        // title: "mmksmkf",
        // value: "1220",
        // name: "José",
        // description: "fnkdnfkjsnkjnskjfnskjfnksjnfkjsfkjsnfkjsn",
        items: [],
        cidades: [],
      }
    },
    mounted() {
      this.getQuartos();
      console.log(this.items)
    //   axios.get('/api/images/1/').then((response) => {
    //   this.imageUrl = response.data.url;
    // });
      // cidadeEscolhida()
      //   if (this.item.cidade === cidade) {
      //     return cidade
      //   }
      },
    methods: {
      getQuartos() {
        this.loading = true
        QuartosApi.getQuartos().then((data) => {
          this.items = data.quartos
          // this.cidades = this.cidades.push(this.items.cidades)
          // this.UrlImg = `https://image.tmdb.org/t/p/original/${this.items.imagem}`
          this.loading = false
        })
      },
      async addNewQuarto(quarto) {
        this.loading = true
        await QuartosApi.addNewQuarto(quarto) 
        this.appStore.showSnackbar(`Novo quarto adicionada #${quarto.id}`)
        this.getQuartos()
        this.loading = false
        console.log("oi")
      },
    },
  }
</script>