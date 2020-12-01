import Vue from "vue";
import Antd from "ant-design-vue";
import VueRouter from "vue-router";
import axios from "axios";

// LINK Style
import "reset-css";
import "ant-design-vue/dist/antd.less";
import "./styles/common.scss";

// LINK component
import App from "./App.vue";
import Routes from "./router/Routes";
import store from "./store";

// LINK Vue 3rdparties
Vue.use(VueRouter);
Vue.use(Antd);
Vue.prototype.$http = axios;

const router = new VueRouter({ routes: Routes, mode: "history" });

new Vue({
  el: "#app",
  components: { App },
  template: "<App/>",
  router,
  store,
});
