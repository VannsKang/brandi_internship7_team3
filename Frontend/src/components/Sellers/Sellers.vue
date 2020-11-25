div<template>
  <a-layout class="sellers">
    <div>
      <sellers-header />

      <!-- SECTION contents -->
      <a-layout-content class="sellers-content">
        <div class="sellers-content-header">
          <div>
            <a-icon type="unordered-list" />
            <span>셀러 회원 리스트</span>
          </div>
          <div>
            <a-button type="primary" size="default">
              <a-icon type="save" theme="filled" />
              <span>엑셀 다운로드</span>
            </a-button>
          </div>
        </div>
        <div class="sellers-content-main">
          <sellers-pagination :data="data" />

          <sellers-table
            :data="data"
            :columns="columns"
            :seller_status="seller_status"
            :seller_attribute_id="seller_attribute_id"
          />

          <sellers-pagination :data="data" />
        </div>
      </a-layout-content>
    </div>
  </a-layout>
</template>

<script>
import SellersPagination from "./Sellers-pagination/Sellers-pagination";
import SellersHeader from "./Sellers-header/Sellers-header";
import SellersTable from "./Sellers-table/Sellers-table";
import { SELLERS_TABLE } from "../../config";

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
      seller_status: [],
      seller_attribute_id: [],
    };
  },

  methods: {
    async loadSellerTable() {
      try {
        const response = await this.$http.get(SELLERS_TABLE);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        const {
          data,
          columns,
          seller_status,
          seller_attribute_id,
        } = await response.data;
        this.data = data;
        this.columns = columns;
        this.seller_status = seller_status;
        this.seller_attribute_id = seller_attribute_id;
      } catch (error) {
        console.log("!!error fetch data!!");
      }
    },
  },

  computed: {},
  // SECTION lifecycle
  mounted() {
    this.loadSellerTable();
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles/mixin.scss";

.sellers {
  overflow: auto;
  > div {
  }
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

    &-main {
    }
  }
}
</style>
