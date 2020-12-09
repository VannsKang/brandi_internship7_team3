<template>
  <a-layout class="sellers">
    <div>
      <sellers-header :header="seller_header" />

      <!-- SECTION contents -->
      <a-layout-content class="sellers-content">
        <div class="sellers-content-header">
          <div>
            <a-icon type="unordered-list" />
            <span>셀러 회원 리스트</span>
          </div>
          <div>
            <a-button type="primary" size="default" @click="downloadExcel">
              <a-icon type="save" theme="filled" />
              <span>엑셀 다운로드</span>
            </a-button>
          </div>
        </div>
        <div class="sellers-content-main">
          <sellers-pagination
            :seller_count="seller_count"
            :page_number="page.page_number"
            :currentPagination="page.currentPagination"
            :controlPagesDrop="controlPagesDrop"
            :controlPages="controlPages"
          />

          <sellers-table
            :data="data"
            :columns="columns"
            :searchInput="searchInput"
            :searchSellerDropdown="searchSellerDropdown"
            :onDateChange="onDateChange"
            :searchData="searchData"
            :submitSearch="submitSearch"
            :resetSearch="resetSearch"
            :handleActions="handleActions"
          />

          <sellers-pagination
            :seller_count="seller_count"
            :page_number="page.page_number"
            :currentPagination="page.currentPagination"
            :controlPagesDrop="controlPagesDrop"
            :controlPages="controlPages"
          />
        </div>
      </a-layout-content>
    </div>
  </a-layout>
  <!-- ANCHOR without Token -->
  <!-- <a-layout v-else>
    <a-result status="404" title="404" sub-title="잘못된 접근입니다!">
      <template #extra>
        <a-button type="primary" @click="backHome" class="backHome">
          로그인 화면으로
        </a-button>
      </template>
    </a-result>
  </a-layout> -->
</template>

<script>
import { mapActions, mapState } from "vuex";

// LINK component
import SellersHeader from "../components/Sellers-header/Sellers-header";
import SellersPagination from "./Sellers-pagination/Sellers-pagination";
import SellersTable from "./Sellers-table/Sellers-table";

// LINK API
import {
  SELLERS_TABLE,
  TABLE_QUERY,
  EXCEL_QUERY,
  ACTION_QEURY,
  SELLER_STATUS,
  SELLER_ATTRIBUTE_ID,
} from "../../config";

export default {
  name: "Sellers",

  components: {
    "sellers-pagination": SellersPagination,
    "sellers-header": SellersHeader,
    "sellers-table": SellersTable,
  },

  data() {
    return {
      data: [],
      columns: [],
      seller_count: 0,

      page: {
        page_number: 1,
        currentPagination: 10,
      },

      searchData: {
        id: "",
        seller_id: "",
        eng_name: "",
        kor_name: "",
        owner_name: "",
        seller_status_id: 0,
        phone_number: "",
        email: "",
        seller_attribute_id: 0,
        start_time: "",
        end_time: "",
      },
    };
  },

  computed: {
    // SECTION vuex
    ...mapState({
      seller_header: ({ sellers }) => sellers.seller_header,
      user_token: ({ users }) => users.user_id,
    }),
  },

  methods: {
    // STUB get seller props
    async getSellerProps(api_adress, callback) {
      try {
        const response = await this.$http.get(api_adress);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        console.log(response);
        const result = response.data;
        callback(result);
      } catch (error) {
        console.log("!!error fetch data!!");
      }
    },

    // STUB basic query table updator
    async getQueryTable(api_adress, query_body) {
      try {
        const response = await this.$http.post(api_adress, query_body);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        console.log(response);
        const { data, columns, seller_count } = await response.data;
        this.data = data;
        this.columns = columns;
        this.seller_count = seller_count;
      } catch (error) {
        console.log("!!error fetch data!!");
      }
    },

    // TODO initilize
    loadSellerTable() {
      const initBody = {
        offset: 0,
        limit: 10,
      };
      this.getQueryTable(SELLERS_TABLE, initBody);
    },

    // TODO pagination
    controlPages(e) {
      const { id } = e.target.dataset;
      id === "minus" && this.page.page_number--;
      id === "plus" && this.page.page_number++;

      //TODO get query string for next page
      const updateBody = {
        offset: (this.page.page_number - 1) * this.page.currentPagination,
        limit: this.page.currentPagination,
      };

      this.getQueryTable(SELLERS_TABLE, updateBody);
    },

    async controlPagesDrop(value) {
      this.page.currentPagination = value;

      const updateBody = {
        offset: 0,
        limit: value,
      };

      this.getQueryTable(SELLERS_TABLE, updateBody);
    },

    //  TODO search query
    getSearchData(value, id) {
      const searchBody = {
        [id]: value,
      };

      this.getQueryTable(SELLERS_TABLE, searchBody);
    },

    searchInput(e) {
      const { value, id } = e.target;
      this[id] = value;
      value === "" ? this.loadSellerTable() : this.getSearchData(value, id);
    },

    searchSellerDropdown(value, e) {
      const { name } = e.data.attrs;
      if (name === "seller_status")
        return (this.searchData.seller_status_id = value);
      if (name === "seller_attribute_id")
        return (this.searchData.seller_attribute_id = value);
    },

    onDateChange(name, date, dateString) {
      if (name === "start_time")
        return (this.searchData.start_time = dateString);
      if (name === "end_time") return (this.searchData.end_time = dateString);
    },

    submitSearch() {
      let searchBody = this.searchData;
      searchBody = {
        ...searchBody,
        offset: 0,
        limit: this.page.currentPagination,
      };
      console.log(searchBody);
      this.getQueryTable(SELLERS_TABLE, searchBody);
    },

    resetSearch() {
      this.searchData = {
        id: "",
        seller_id: "",
        eng_name: "",
        kor_name: "",
        owner_name: "",
        seller_status: 0,
        phone_number: "",
        email: "",
        seller_attribute_id: 0,
        start_time: "",
        end_time: "",
      };

      const updateBody = {
        offset: 0,
        limit: this.page.currentPagination,
      };
      this.getQueryTable(SELLERS_TABLE, updateBody);
    },

    // STUB action handler
    async getAction(api_adress, query_body) {
      try {
        const response = await this.$http.put(api_adress, query_body);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        console.log(response);
        const { data, columns, seller_count } = await response.data;
        this.data = data;
        this.columns = columns;
        this.seller_count = seller_count;
      } catch (error) {
        console.log("!!error fetch data!!");
      }
    },

    async handleActions(e) {
      const { id, btn } = e.target.dataset;
      console.log(id, btn);
      const actionBody = {
        id: id,
        seller_action_id: +btn,
      };
      const updateBody = {
        offset: 0,
        limit: this.page.currentPagination,
      };
      // NOTE action applied
      await this.getAction(ACTION_QEURY, actionBody);
      // NOTE update table
      await this.getQueryTable(TABLE_QUERY, updateBody);
    },

    //  TODO Excel download
    async downloadExcel() {
      try {
        this.$http({
    method: 'POST',
    url: "http://localhost:5000/seller_info/download",
    responseType: 'blob',
    headers: {
        "Content-Type": "application/json"
    },   
    data: {
     
    } 
})
.then((response) => {
    const url = window.URL.createObjectURL(new Blob([response.data], { type: response.headers['content-type'] }));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'test.csv');
    document.body.appendChild(link);
    link.click();
})
        // const response = await this.$http.post(EXCEL_QUERY, {});
        // // const url = window.URL.createObjectURL(new Blob([response.data]));
        // // const link = document.createElement("a");
        // // link.href = url;
        // // link.setAttribute("download", "template.xlsx");
        // // document.body.appendChild(link);
        // // link.click();
        // const url = window.URL.createObjectURL(
        //   new Blob([response.data], {
        //     type: response.headers["content-type"],
        //   })
        // );
        // const link = document.createElement("a");
        // link.href = url;
        // link.setAttribute("download", "test.xlsx");
        // document.body.appendChild(link);
        // link.click();
      } catch (error) {
        console.log("!!!error!!!");
      }

      // console.log(response);
      // let table = document.querySelector(".sellers-content-main-table")
      //   .innerHTML;
      // table = table.replace(/<input[^>]*>|<\/input>/gi, ""); // reomves input params
      // table = table.replace(/<button[^>]*>|<\/button>/gi, ""); // reomves button params
      // table = table.replace(/<select[^>]*>|<\/select>/gi, ""); // reomves select params
      // table = table.replace(/<tr[^<>]*>(.(?!<tr[^<>]*>))*?<\/tr>/, ""); //remove first row
      // table = table.replace(/<td(([^<]|<(?!\/td>))*)<\/td>\s*<\/tr>/g, ""); //remove last column
      // window.open(`data:application/vnd.ms-excel,${encodeURIComponent(table)}`);
    },

    // ANCHOR no token action
    backHome() {
      this.$router.push("/");
    },

    // SECTION vuex
    ...mapActions("sellers", [
      "updateSellerStatusAction",
      "updateSellerAttributeAction",
    ]),
  },

  // SECTION lifecycle
  mounted() {
    this.loadSellerTable();
    // NOTE getSELLER_STATUS
    this.getSellerProps(SELLER_STATUS, this.updateSellerStatusAction);
    // NOTE getSELLER_ATTRIBUTE_ID
    this.getSellerProps(SELLER_ATTRIBUTE_ID, this.updateSellerAttributeAction);
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles/mixin.scss";

.sellers {
  overflow: auto;

  &-content {
    margin: 10px 20px 45px;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 4px;

    &-header {
      width: 100%;
      height: 38px;
      padding: 0 10px;
      border-radius: 4px 4px 0 0;
      background: #eee;

      @include flexSet("space-between", "center");

      > div {
        @include flexSet("flex-start", "center");

        &:first-child {
          color: #111;

          span {
            margin-left: 5px;
            font-size: 16px;
          }
        }

        &:last-child {
          > button {
            background: $excel-button-color;
            border: 1px solid $excel-button-color;
            padding: 0 10px;
          }
        }
      }
    }
  }
}

.backHome {
  background: $nav-side-color;
  border: $nav-side-color;
}
</style>
