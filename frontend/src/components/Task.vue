<template>
  <v-card>
    <v-card-text>
      <div>#{{ task.id }}</div>
      <p class="ma-0 pa-0 text-h5 text--primary">
        {{ task }}
        {{ task.description }}
      </p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "TasksModel",
  props: {
    task: {
      type: Object,
      default: null,
      roger: "usalinter",
    },
  },
  data: () => ({}),
  mounted() {
    console.log(this.task)
    console.log(this.task.id)
  },
}
</script>
