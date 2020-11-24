import Vue from "vue";
import Antd from "ant-design-vue";
import VueRouter from "vue-router";

// LINK Style
import "reset-css";
import "ant-design-vue/dist/antd.less";
import "./styles.scss";

// LINK component
import App from "./App.vue";
import Routes from "./router/Routes";

// LINK Vue 3rdparties
Vue.use(VueRouter);
Vue.use(Antd);

const router = new VueRouter({ routes: Routes, mode: "history" });

new Vue({
  el: "#app",
  components: { App },
  template: "<App/>",
  router,
});
