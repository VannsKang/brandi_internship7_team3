<template>
  <a-row class="logo-section">
    <div class="logo">
      <router-link to="/" exact>
        <img :src="logoImage" alt="" />
      </router-link>
    </div>
  </a-row>
</template>

<script>
import logoImage from "../../../assets/logo_seller_admin.png";

export default {
  name: "Login-logo",

  data() {
    return {
      logoImage,
    };
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/mixin.scss";

.logo-section {
  @include flexSet("center", "center");

  .logo {
    width: 130px;
    margin-bottom: 40px;

    img {
      width: 100%;
    }
  }
}
</style>
