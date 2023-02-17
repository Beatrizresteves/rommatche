<template>
  <v-container color="#5DCAD1">
    <app-nav-bar/>
    <chats-view/>
  </v-container>
</template>
<script>
import AppNavBar from '../../components/AppNavBar.vue'
import ChatsView from '../../components/ChatsView.vue'
  export default {
  components: { ChatsView, AppNavBar },
  }
</script>
