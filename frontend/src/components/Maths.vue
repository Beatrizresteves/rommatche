<template>
  <h1>teste</h1>
  <v-card>
    <v-card-text>
      <div>#{{ quartos }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
      teste  ssd{{ quartos }}
      </p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "QuartosModel",
  props: {
    quarto: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({}),
}
</script>