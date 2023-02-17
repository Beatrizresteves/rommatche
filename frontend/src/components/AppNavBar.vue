<template>
  <v-app-bar color="#5DCAD1">
      <v-toolbar-title> <v-img class="mt-5" width="120" heigth="100%" src="@/assets/logo.png" @click="redirectToPage"/></v-toolbar-title>
    <template #append>
      <!-- <v-btn icon="mdi-heart" :to="{ name: 'base-home' }"></v-btn>
      <v-btn icon="mdi-magnify"></v-btn> -->
      <!-- <v-btn
        v-if="loggedUser"
        background-color="rgb(236 243 243)"
        min-width="140"
        height="40px"
        rel="noopener noreferrer"
        size="x-large"
        variant="flat"
        :to="{ name: 'accounts-login' }"
        rounded
        class="my-4">
        <v-img width="30px" class="mr-2" src="@/assets/icone.png"/>
        Likes
      </v-btn> -->
      <v-btn
        icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list>
            <v-list-item :to="{ name: 'accounts-logout' }"> Sair </v-list-item>
            <v-list-item :to="{ name: 'base-likes' }"> Likes </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: false,
      default: "MyApp",
    },
    theme: {
      type: String,
      required: true,
      default: "light",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {}
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
    redirectToPage() {
      this.$router.push({ name: 'base-home' });
    }
  },
}
</script>
<style scoped>
.body {
background-color:#5DCAD1;
}
#app-bar {
color: #5DCAD1;
background-color: aliceblue;
}

</style>