<template>
  <a-layout class="sellerInfo">
    <div>
      <sellers-header :header="sellerInfo_header" />

      <a-layout-content class="sellerInfo-content">
        <div class="sellerInfo-content-header">
          <div>
            <a-icon type="user" />
            <span>기본 정보</span>
          </div>
        </div>
        <!-- TODO content -->
        <!-- html작성 -->
      </a-layout-content>
    </div>
  </a-layout>
</template>

<script>
import { mapState } from "vuex";

// LINK component
import SellersHeader from "../components/Sellers-header/Sellers-header";

export default {
  name: "SellerInfo",

  components: {
    "sellers-header": SellersHeader,
  },

  data() {
    return {
      // state관리
    };
  },

  computed: {
    ...mapState({
      sellerInfo_header: ({ sellerInfo }) => sellerInfo.sellerInfo_header,
    }),
  },

  methods: {
    // 함수
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles/mixin.scss";

.sellerInfo {
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
      }
    }
  }
}

/* 여기다 css */
</style>
