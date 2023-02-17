<template>
  <v-container color="#5DCAD1">
    <app-nav-bar/>
  <div class="d-flex flex-row-reverse w-140">
      <v-btn
        offset-sm="3"
        color="#4bf9f9"
        min-width="140"
        height="40px"
        rel="noopener noreferrer"
        size="x-large"
        variant="flat"
        :to="{ name: 'base-likes' }"
        rounded
        class=" ml-5">
        <v-img width="30px" class="mr-2" src="@/assets/icone.png"/>
        Likes
      </v-btn>
    </div>
    <search-citys/>
    <rooms-match/>
  </v-container>
</template>


<script >
import AppNavBar from "@/components/AppNavBar.vue"
import SearchCitys from '../../components/SearchCitys.vue'
import RoomsMatch from '../../components/RoomsMatch.vue'

export default {
  components: { AppNavBar, SearchCitys, RoomsMatch },
}
</script>
