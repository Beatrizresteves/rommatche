<template>
  <v-container color="#5DCAD1">
    <app-nav-bar/>
    <match-form/>

  </v-container>
</template>


<script >
import AppNavBar from "@/components/AppNavBar.vue"
import MatchForm from '../../components/MatchForm.vue'

export default {
  components: { AppNavBar, MatchForm },
}
</script>
