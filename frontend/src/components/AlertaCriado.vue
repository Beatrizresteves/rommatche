<!-- eslint-disable vue/require-default-prop -->
<template>
   <v-alert color="primary" type="success">
      {{ msg }}
    </v-alert>
</template>

<script>
export default {
  name: "AlertaCriado",
  props: {
    // eslint-disable-next-line vue/require-default-prop
    msg: String,
  },
};
</script>

<style>

</style>