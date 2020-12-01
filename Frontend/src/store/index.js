import Vue from "vue";
import Vuex from "vuex";
import VuexPersist from "vuex-persist";
import createLogger from "vuex/dist/logger";

// LINK vuex modules
import users from "./modules/users";
import navmenus from "./modules/navmenus";
import sellers from "./modules/sellers";
import sellerInfo from "./modules/sellerInfo";

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== "production";

const vuexLocalStorage = new VuexPersist({
  key: "STORAGE_KEY",
  storage: window.localStorage,
  reducer: (state) => ({
    users: state.users,
  }),
});

export default new Vuex.Store({
  modules: {
    users,
    navmenus,
    sellers,
    sellerInfo,
  },
  strict: debug,
  plugins: debug ? [createLogger(), vuexLocalStorage.plugin] : [],
});
