<template>
  <v-container class="fill-height">
    <app-nav-bar :theme="theme" @theme-click="onThemeClick"></app-nav-bar>
    <v-responsive class="d-flex align-center text-center fill-height">
      <h2 color="#5DCAD1">Bem-vindo à plataforma que irá ajudar você encontrar o seu vizinho de quarto ideal!</h2>
      <!-- <div class="text-body-1 mb-n1 pt-4">Bem-vindo à plataforma que irá ajudar você encontrar o seu vizinho de quarto ideal!</div> -->
      <div class="d-inline-block">
        <v-img width="520px" class="" src="@/assets/logo2.png" />
      </div>

      <div />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            v-if="loggedUser"
            color="primary"
            :to="{ name: 'base-getstarted' }"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            rounded
            class="my-4 mr-2">
              <v-icon class="mr-1">mdi-magnify</v-icon>
            Procurar quarto
          </v-btn>
          <v-btn
            v-if="loggedUser"
            color="#5DCAD1"
            :to="{ name: 'base-getregister' }"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            rounded
            class="my-4">
              <v-icon class="mr-1">mdi-pencil</v-icon>
            Cadastrar quarto
          </v-btn>
          <v-btn
            v-if="!loggedUser"
            color="#5DCAD1"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-register' }"
            rounded
            class="my-4 mr-2">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Criar uma conta
          </v-btn>
          <v-btn
            v-if="!loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            rounded
            class="my-4">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Login
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import AppNavBar from "@/components/AppNavBar.vue"

export default {
  components: {
    AppNavBar,
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
}
</script>
