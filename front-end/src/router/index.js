import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue"
import Settings from "../views/Settings.vue";
import Translate from "../views/Translate.vue"
import DashBoard from "../views/DashBoard.vue"
import { authGuard } from "../auth";
import Lesson from '../views/Lesson.vue';


Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/settings",
      name: "settings",
      component: Settings,
      beforeEnter: authGuard
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashBoard,
      beforeEnter: authGuard
    },
    {
      path: "/Profile",
      name: "Profile",
      component: Profile,
      beforeEnter: authGuard
    },
    {
      path: "/translate",
      name: "translate",
      component: Translate,
      beforeEnter: authGuard
    },
    //Testing new route
    {
      path:'/lesson',
      name:'lesson',
      component:Lesson,
      beforeEnter:authGuard
    }
  ]
});

export default router;
