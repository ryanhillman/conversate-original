import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import { Auth0Plugin } from "./auth";
import hljs from "highlight.js/lib/core";
import "highlight.js/styles/github.css";

import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { domain, clientId } from "../auth_config.json";


import translate from "translate";
translate.engine = "libre";


import axios from "axios";
// Set the axios base URL, this will need to be changed for production
axios.defaults.baseURL = "http://localhost:5000";
axios.defaults.headers = {
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Allow-Origin": "*"
};
axios.defaults.mode = "cors";


Vue.config.productionTip = false;

Vue.use(hljs.vuePlugin);

Vue.use(Auth0Plugin, {
  domain,
  clientId,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

library.add(fas);
Vue.component("font-awesome-icon", FontAwesomeIcon);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
