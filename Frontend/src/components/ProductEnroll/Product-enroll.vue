<template>
  <div class="product-enroll">
    <sellers-header :header="product_enroll_header" />
    <a-layout-content class="product-enroll-content">
      <img :src="poastImg" alt="postman" />
    </a-layout-content>
  </div>
</template>

<script>
import SellersHeader from "../components/Sellers-header/Sellers-header";
import { mapState } from "vuex";
import postman from "../../assets/postman.png";

export default {
  name: "Product-enroll",

  components: {
    "sellers-header": SellersHeader,
  },

  data() {
    return {
      poastImg: postman,
    };
  },

  computed: {
    // SECTION vuex
    ...mapState({
      user_token: ({ sellerInfo }) => sellerInfo.product_enroll_header,
    }),
  },
};
</script>

<style lang="scss" scoped>
.product-enroll {
  overflow: auto;

  &-content {
    margin: 10px 20px 45px;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    > img {
      width: 100%;
    }
  }
}
</style>
