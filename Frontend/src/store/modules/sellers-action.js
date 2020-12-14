import axios from "axios";
import Swal from "sweetalert2";

// LINK API
import {
  SELLER_STATUS,
  SELLERS_TABLE,
  SELLER_ATTRIBUTE_ID,
  ACTION_QUERY,
  EXCEL_QUERY,
} from "../../config";

export const actions = {
  // SECTION update seller props

  // STUB get seller props
  async getSellerProps({ commit }, mutation, api_adress) {
    try {
      const response = await axios.get(api_adress);
      const validation = response && response.status === 200;
      !validation && new Error("cannot fetch the data");
      console.log(response);
      const result = response.data;
      commit(mutation, result);
    } catch (error) {
      console.log("!!error fetch data!!");
    }
  },

  updateSellerStatusAction({ commit, state }) {
    if (state.seller_status.length === 0) {
      actions.getSellerProps({ commit }, "updateSellerStatus", SELLER_STATUS);
    }
  },

  updateSellerAttributeAction({ commit, state }) {
    // REVIEW version management!
    if (state.seller_attribute_id.length === 0) {
      actions.getSellerProps(
        { commit },
        "updateSellerAttribute",
        SELLER_ATTRIBUTE_ID
      );
    }
  },

  // SECTION update Table

  // STUB basic query table updator
  async queryTable({ commit, rootState }, api_adress, query_body) {
    try {
      // NOTE mockdata
      // const response = await axios.get(api_adress);
      // NOTE backend
      const user_token = await rootState.users.user_token;
      const headers = {
        headers: {
          Authorization: user_token,
        },
      };
      const response = await axios.post(api_adress, query_body, headers);
      const validation = response && response.status === 200;
      !validation && new Error("cannot fetch the data");
      console.log(response);
      const result = await response.data;
      commit("changeLoadingFalse");
      commit("updateTable", result);
    } catch (error) {
      console.log("!!error fetch data!!");
      const user_token = await rootState.users.user_token;
      if (user_token) {
        Swal.fire({
          title: "검색 결과가 없습니다!",
          timer: 2000,
          icon: "error",
          showConfirmButton: false,
        });
        commit("changeLoadingFalse");
      }
    }
  },

  //  STUB search query
  searchData({ commit, rootState }, value, id) {
    commit("changeLoadingTrue");
    const searchBody = {
      [id]: value,
    };
    actions.queryTable({ commit, rootState }, SELLERS_TABLE, searchBody);
  },

  // STUB store update for multisearch
  inputState({ commit }, value, id) {
    const stateItems = {
      [id]: value,
    };
    console.log(stateItems);
    commit("updateSearchInput", stateItems);
  },

  // TODO initilize
  initTableAction({ commit, rootState }) {
    commit("changeLoadingTrue");
    const initBody = {
      offset: 0,
      limit: 10,
    };
    actions.queryTable({ commit, rootState }, SELLERS_TABLE, initBody);
  },

  // TODO search
  searchInput({ commit, rootState }, e) {
    const { value, id } = e.target;
    if (value === "") {
      commit("resetSearchInput");
      commit("resetPage");
      actions.initTableAction({ commit, rootState });
    } else {
      commit("resetPage");
      actions.searchData({ commit, rootState }, value, id);
    }
  },

  sellerStatusDropdown({ commit }, value) {
    actions.inputState({ commit }, value, "seller_status_id");
  },

  sellerAttributeDropdown({ commit }, value) {
    actions.inputState({ commit }, value, "seller_attribute_id");
  },

  getStartTime({ commit }, date) {
    const formatedDate = date.format("YYYY-MM-DD");
    actions.inputState({ commit }, formatedDate, "start_time");
  },

  getEndTime({ commit }, date) {
    const formatedDate = date.format("YYYY-MM-DD");
    actions.inputState({ commit }, formatedDate, "end_time");
  },

  updateSearchState({ commit }, e) {
    const { value, id } = e.target;
    actions.inputState({ commit }, value, id);
  },

  // TODO submit, reset
  submitSearch({ commit, state, rootState }) {
    commit("changeLoadingTrue");
    let searchBody = state.search_input;
    searchBody = {
      ...searchBody,
      offset: 0,
      limit: state.page.currentPagination,
    };
    actions.queryTable({ commit, rootState }, SELLERS_TABLE, searchBody);
  },

  resetSearch({ commit, state, rootState }) {
    commit("changeLoadingTrue");
    commit("resetSearchInput");
    commit("resetPage");
    const updateBody = {
      offset: 0,
      limit: state.page.currentPagination,
    };
    actions.queryTable({ commit, rootState }, SELLERS_TABLE, updateBody);
  },

  // TODO pagination
  controlPagesAction({ commit, state, rootState }, e) {
    commit("changeLoadingTrue");
    const { id } = e.target.dataset;
    commit("controlPages", id);
    //TODO get query string for next page
    const updateBody = {
      offset: (state.page.page_number - 1) * state.page.currentPagination,
      limit: state.page.currentPagination,
    };
    actions.queryTable({ commit, rootState }, SELLERS_TABLE, updateBody);
  },

  controlPagesDrop({ commit, state, rootState }, value) {
    commit("changeLoadingTrue");
    commit("resetPage");
    commit("updatePagination", value);
    const updateBody = {
      offset: (state.page.page_number - 1) * value,
      limit: value,
    };
    // commit("matchPage");
    actions.queryTable({ commit, rootState }, SELLERS_TABLE, updateBody);
  },

  // TODO action handler

  // STUB action handler
  async queryAction({ commit, rootState }, api_adress, query_body) {
    try {
      const user_token = await rootState.users.user_token;
      const headers = {
        headers: {
          Authorization: user_token,
        },
      };
      const response = await axios.put(api_adress, query_body, headers);
      const validation = response && response.status === 200;
      !validation && new Error("cannot fetch the data");
      console.log(response);
      const result = await response.data;
      commit("changeLoadingFalse");
      commit("updateTable", result);
    } catch (error) {
      console.log("!!error fetch data!!");
    }
  },

  async updateAction({ commit, state, rootState }, e) {
    commit("changeLoadingTrue");
    const { id, btn } = e.target.dataset;
    console.log(id, btn);
    const actionBody = {
      id: id,
      seller_action_id: +btn,
    };
    const updateBody = {
      offset: 0,
      limit: state.page.currentPagination,
    };
    // NOTE action applied
    await actions.queryAction({ commit, rootState }, ACTION_QUERY, actionBody);
    // NOTE update table with reset pagenumber
    commit("resetPage");
    actions.queryTable({ commit, rootState }, SELLERS_TABLE, updateBody);
  },

  // TODO checkbox control
  changeEachCheckBox({ commit }, e) {
    // const { checked, id } = e.target;
    const checkedStatus = e.target;

    commit("updateCheckedList", checkedStatus);
  },

  onCheckAllChange({ commit }, e) {
    const { checked } = e.target;

    const eachInput = document.querySelectorAll(".listItems");
    eachInput.forEach((item) =>
      checked
        ? item.childNodes[0].classList.add("ant-checkbox-checked")
        : item.childNodes[0].classList.remove("ant-checkbox-checked")
    );

    commit("updateCheckAll", checked);
  },

  getCheckboxId({ commit }) {
    commit("updateCheckBoxId");
  },

  // TODO excel download
  async downloadExcel({ rootState }) {
    try {
      const user_token = await rootState.users.user_token;

      axios({
        method: "POST",
        url: EXCEL_QUERY,
        responseType: "blob",
        headers: {
          Authorization: user_token,
          "Content-Type": "application/json",
        },
        data: {},
      }).then((response) => {
        const url = window.URL.createObjectURL(
          new Blob([response.data], {
            type: response.headers["content-type"],
          })
        );
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "test.csv");
        document.body.appendChild(link);
        link.click();
      });
    } catch (error) {
      console.log("!!!error!!!");
    }
  },
};
