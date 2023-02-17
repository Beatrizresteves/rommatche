<template>
  <v-card
    class="mx-auto mt-10"
    max-width="500"
	>
    <v-toolbar color="primary">
      <v-btn variant="text" icon="mdi-menu"></v-btn>

      <v-toolbar-title>Inbox </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn variant="text" icon="mdi-magnify"></v-btn>
    </v-toolbar>

    <v-list
      :items="items"
      item-props
      lines="three"
    >
      <template v-slot:subtitle="{ subtitle }">
        <div v-html="subtitle"></div>
      </template>
    </v-list>
  </v-card>
</template>
<script>
  export default {
    data: () => ({
      items: [
        { type: 'subheader', title: 'Today' },
        {
          prependAvatar: 'https://images.pexels.com/photos/172872/pexels-photo-172872.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
          title: 'Ana Lúcia',
          subtitle: `Deseja conhecer o apartamento?`,
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://images.pexels.com/photos/3555619/pexels-photo-3555619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
          title: 'Luiza',
          subtitle: `<span class="text-primary">Você </span> &mdash; O que está incluso no valor?`,
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://images.pexels.com/photos/2029687/pexels-photo-2029687.jpeg?auto=compress&cs=tinysrgb&w=1600',
          title: 'Antonia',
          subtitle: `<span class="text-primary">Você </span> &mdash; Qual o endereço do apartamento?`,
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://images.pexels.com/photos/4112553/pexels-photo-4112553.jpeg?auto=compress&cs=tinysrgb&w=1600',
          title: 'Mariana',
          subtitle: 'No valor está incluso contas de água, luz e wifi.',
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://images.pexels.com/photos/2416931/pexels-photo-2416931.jpeg?auto=compress&cs=tinysrgb&w=1600',
          title: 'Maia',
          subtitle: 'O quarto é excelente, você vai adorar. Quer vim conhcer?',
        },
      ],
    }),
  }
</script>