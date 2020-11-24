<template>
  <section class="main-top">
    <div class="main-top-logo">
      <router-link to="/main" exact>
        <img :src="logoImg" alt="logo" />
      </router-link>
    </div>
    <div class="main-top-user">
      <a-dropdown placement="bottomRight">
        <div>
          <span>intern_master</span>
          <a-icon type="down" />
        </div>
        <a-menu class="main-top-user-menu" slot="overlay">
          <a-menu-item>
            <a-icon type="key" />
            <span>Log Out</span>
          </a-menu-item>
        </a-menu>
      </a-dropdown>
    </div>
  </section>
</template>

<script>
import logoImg from "../../../assets/nav_logo.png";

export default {
  name: "Main-top",
  data() {
    return {
      placements: ["bottomRight"],
      logoImg,
    };
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles.scss";

.main-top {
  width: 100%;
  height: 45px;
  background: $nav-color;
  padding: 0 20px;
  @include flexSet("space-between", "center");

  &-logo {
    width: 100px;
    img {
      width: 100%;
      height: 100%;
    }
  }

  &-user {
    width: 126px;
    height: 100%;
    padding-left: 5px;
    border-left: 1px solid #484a4f;
    cursor: pointer;

    > div {
      @include flexSet("center", "center");
      height: 100%;
      color: #ddd;

      &:hover {
        background: #484a4f;
      }
      > span {
        margin-right: 5px;
      }
    }

    &-menu {
      width: 158px;
      height: 40px;
      > li {
        &:hover {
          background: #eee;
        }
      }
    }
  }
}
</style>
