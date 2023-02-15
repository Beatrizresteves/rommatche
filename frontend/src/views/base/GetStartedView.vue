<template>
  <v-container color="#5DCAD1">
    <app-nav-bar/>
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
    <search-citys/>
    <rooms-match/>
    <maths/>
  </v-container>
</template>


<script >
import AppNavBar from "@/components/AppNavBar.vue"
import SearchCitys from '../../components/SearchCitys.vue'
import RoomsMatch from '../../components/RoomsMatch.vue'
import Maths from '../../components/Maths.vue'

export default {
  components: { AppNavBar, SearchCitys, RoomsMatch, Maths },
}
</script>
