// SECTION initial state
const state = () => ({
  seller_header: {
    title: "셀러 계정 관리",
    sub_title: "셀러 회원 목록 / 관리",
    breadcrumb: ["회원 관리", "셀러 계정 관리", "셀러 회원 리스트"],
  },

  seller_status: [],

  seller_attribute_id: [],

  pageControl: [10, 20, 50, 100, 150],

  input_value: "",
  select_value: "Select",
});

// SECTION getters
const getters = {
  //
};

// mutations
const mutations = {
  updateSellerStatus(state, payload) {
    state.seller_status = payload;
  },

  updateSellerAttribute(state, payload) {
    state.seller_attribute_id = payload;
  },
};

// actions
const actions = {
  updateSellerStatusAction({ commit }, payload) {
    commit("updateSellerStatus", payload);
  },

  updateSellerAttributeAction({ commit }, payload) {
    commit("updateSellerAttribute", payload);
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
