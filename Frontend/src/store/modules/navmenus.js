import axios from "axios";
import { FOOTER_DATA, NAV_MENU_DATA } from "../../config";

// SECTION initial state
const state = () => ({
  // SECTION menuItems
  menuItems: [],

  // SECTION footer
  footer_text: "",

  copyright: "",

  email: "",
});

// getters
const getters = {
  //
};

// mutations
const mutations = {
  updateFooter(state, payload) {
    state.footer_text = payload.footer_text;
    state.copyright = payload.copyright;
    state.email = payload.email;
  },

  updateMenu(state, payload) {
    state.menuItems = payload.menuItems;
  },
};

// actions
const actions = {
  async updateFooterAction({ commit }) {
    // REVIEW version management!
    if (!state.footer_text || !state.copyright) {
      try {
        const response = await axios.get(FOOTER_DATA);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        const result = response.data;
        commit("updateFooter", result);
      } catch (error) {
        console.log("!!error fetch data!!");
      }
    }
  },

  async updateMenuAction({ commit }) {
    // REVIEW version management!
    if (!state.menuItems) {
      try {
        const response = await axios.get(NAV_MENU_DATA);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        const result = response.data;
        commit("updateMenu", result);
      } catch (error) {
        console.log("!!error fetch data!!");
      }
    }
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
