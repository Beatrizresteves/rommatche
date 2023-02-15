<template>
  <v-card>
    <v-card-text>
      <div>#{{ quarto.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ quarto.description }}
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