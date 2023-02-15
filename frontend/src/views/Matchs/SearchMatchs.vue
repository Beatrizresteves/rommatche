<template>
  <app-nav-bar>
    dfdfld
</template>
<script>
import { useAppStore } from "@/stores/appStore"
import AppNavBar from "@/components/AppNavBar.vue"

export default {
  components: { AppNavBar },
  setup() {
    const appStore = useAppStore()
	return { appStore }
  },
}
</script>
