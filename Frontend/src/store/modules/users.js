// SECTION initial state
const state = () => ({
  user_token: "",
  user_id: "",
});

// getters
const getters = {
  // cartProducts: (state, getters, rootState) => {
  //   return state.items.map(({ id, quantity }) => {
  //     const product = rootState.products.all.find(product => product.id === id)
  //     return {
  //       title: product.title,
  //       price: product.price,
  //       quantity
  //     }
  //   })
  // },
  // cartTotalPrice: (state, getters) => {
  //   return getters.cartProducts.reduce((total, product) => {
  //     return total + product.price * product.quantity
  //   }, 0)
  // }
};

// mutations
const mutations = {
  getToken(state, payload) {
    console.log(state, payload);
    state.user_token = payload.token;
    state.user_id = payload.user_id;
  },

  removeToken(state) {
    state.user_token = "";
    state.user_id = "";
  },
};

// actions
const actions = {
  getTokenAction({ commit }, payload) {
    commit("getToken", payload);
  },

  removeTokenAction({ commit }) {
    commit("removeToken");
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
