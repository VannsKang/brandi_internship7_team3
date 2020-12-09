// LINK actions
import { actions } from "./sellers-action";

// SECTION initial state
const state = () => ({
  // SECTION seller header data
  seller_header: {
    title: "셀러 계정 관리",
    sub_title: "셀러 회원 목록 / 관리",
    breadcrumb: ["회원 관리", "셀러 계정 관리", "셀러 회원 리스트"],
  },

  // SECTION table items
  data: [],

  columns: [],

  seller_count: 0,

  seller_status: [],

  seller_attribute_id: [],

  // SECTION search control
  input_value: "",
  select_value: "Select",

  search_input: {
    id: "",
    seller_id: "",
    eng_name: "",
    kor_name: "",
    owner_name: "",
    seller_status_id: "Select",
    phone_number: "",
    email: "",
    seller_attribute_id: "Select",
    start_time: "",
    end_time: "",
  },

  // SECTION pagination
  pageControl: [10, 20, 50, 100, 150],

  page: {
    page_number: 1,
    currentPagination: 10,
  },

  // SECTION list select
  indeterminate: false,
  checkAll: false,
  plainOptions: [],
  checkedList: [],

  // SECTION loading
  isLoading: false,
});

// SECTION getters
const getters = {
  max_page: (state) =>
    Math.ceil(state.seller_count / state.page.currentPagination),
};

// mutations
const mutations = {
  updateSellerStatus(state, payload) {
    state.seller_status = payload;
  },

  updateSellerAttribute(state, payload) {
    state.seller_attribute_id = payload;
  },

  updateTable(state, payload) {
    state.data = payload.data;
    state.columns = payload.columns;
    state.seller_count = payload.seller_count;
  },

  updateSearchInput(state, payload) {
    const key = Object.keys(payload)[0];
    state.search_input[key] = payload[key];
  },

  resetSearchInput(state) {
    state.search_input = {
      id: "",
      seller_id: "",
      eng_name: "",
      kor_name: "",
      owner_name: "",
      seller_status_id: "Select",
      phone_number: "",
      email: "",
      seller_attribute_id: "Select",
      start_time: null,
      end_time: null,
    };
  },

  controlPages(state, payload) {
    payload === "minus" && state.page.page_number--;
    payload === "plus" && state.page.page_number++;
  },

  updateCheckedList(state, payload) {
    if (payload.checked) {
      state.checkedList = [...state.checkedList, +payload.id];
    } else {
      state.checkedList = state.checkedList.filter(
        (checkItem) => checkItem !== +payload.id
      );
    }
    state.indeterminate =
      !!state.checkedList.length &&
      +state.checkedList.length < state.plainOptions.length;
    state.checkAll = state.checkedList.length === state.plainOptions.length;
  },

  updateCheckAll(state, payload) {
    state.checkedList = payload ? state.plainOptions : [];
    state.indeterminate = false;
    state.checkAll = payload;
  },

  updateCheckBoxId(state) {
    const allDataId = state.data.map((item) => item.id);
    state.plainOptions = allDataId;
  },

  // SECTION loading

  changeLoadingTrue(state) {
    state.isLoading = true;
  },

  changeLoadingFalse(state) {
    state.isLoading = false;
  },

  // SECTION page control

  resetPage(state) {
    state.page.page_number = 1;
  },

  matchPage(state) {
    state.page.page_number = Math.ceil(
      state.seller_count / state.page.currentPagination
    );
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
