// Composables
import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import HomeView from "@/views/base/HomeView.vue"
import GetStartedView from "@/views/base/GetStartedView.vue"
import GetRegisterView from "@/views/base/GetRegisterView.vue"

export default [
  {
    path: "/",
    component: EmptyLayout,
    children: [
      {
        path: "",
        name: "base-home",
        component: HomeView,
      },
      {
        path: "getstarted",
        name: "base-getstarted",
        component: GetStartedView,
      },
      {
        path: "getregister",
        name: "base-getregister",
        component: GetRegisterView,
      }
    ],
  },
]
