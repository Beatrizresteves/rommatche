// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import GetStartedView from "@/views/base/GetStartedView"
import MatchsView from "@/views/base/GetStartedView"

export default [
  {
    path: "/quartos",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "quartos-list",
        component: GetStartedView,
      },
      {
        path: "matchs",
        name: "quartos-matchs",
        component: MatchsView,
      },
    ],
  },
]
