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
          <sellers-pagination />

          <sellers-table />

          <sellers-pagination />
        </div>
      </a-layout-content>
    </div>
    <div v-if="isLoading" class="loading">
      <div class="loading-background">
        <rise-loader color="#35363a" />
      </div>
    </div>
  </a-layout>
</template>

<script>
import { mapState, mapActions } from "vuex";

// LINK component
import SellersHeader from "../components/Sellers-header/Sellers-header";
import SellersPagination from "./Sellers-pagination/Sellers-pagination";
import SellersTable from "./Sellers-table/Sellers-table";
import RiseLoader from "vue-spinner/src/RiseLoader.vue";

export default {
  name: "Sellers",

  components: {
    SellersPagination,
    SellersHeader,
    SellersTable,
    RiseLoader,
  },

  data() {
    return {};
  },

  computed: {
    // SECTION vuex
    ...mapState({
      seller_header: ({ sellers }) => sellers.seller_header,
      isLoading: ({ sellers }) => sellers.isLoading,
      user_token: ({ users }) => users.user_token,
    }),
  },

  methods: {
    // SECTION vuex
    ...mapActions("sellers", ["downloadExcel"]),
  },
};
</script>

<style src="./Sellers.scss" lang="scss" scoped />
