<template>
  <div class="sellers-content-main-pagination">
    <span>Page</span>
    <div class="sellers-content-main-pagination-button">
      <a-button
        data-id="minus"
        @click="controlPages"
        :disabled="number.value <= 1"
      >
        <a-icon type="left" />
      </a-button>
      <a-input-number v-model="number.value" />
      <a-button data-id="plus" @click="controlPages">
        <a-icon type="right" />
      </a-button>
    </div>
    <span>of {{ Math.floor(data.length / currentPage) }} | View</span>
    <a-select
      class="sellers-content-main-pagination-group"
      :default-value="currentPage"
      @change="controlPagesDrop"
    >
      <a-select-option
        v-for="(page, idx) in pageControl"
        :value="page"
        :key="idx"
      >
        {{ page }}
      </a-select-option>
    </a-select>
    <span>records | Found total {{ data.length }} records</span>
  </div>
</template>

<script>
const pageControl = [10, 20, 50, 100, 150];
export default {
  name: "Sellers-pagination",

  props: {
    data: {
      type: Array,
      required: true,
    },
  },

  data() {
    return {
      number: {
        value: 1,
      },
      pageControl,
      currentPage: 10,
    };
  },

  methods: {
    controlPages(e) {
      const { id } = e.target.dataset;
      id === "minus" && this.number.value--;
      id === "plus" && this.number.value++;

      //TODO get query string for next page
    },

    controlPagesDrop(value) {
      console.log(value);
      this.currentPage = value;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/mixin.scss";

.sellers-content-main-pagination {
  @include flexSet("flex-start", "center");
  margin: 10px;
  color: #111;

  &-button {
    width: 110px;
    margin: 0 10px;
    @include flexSet("space-between", "center");

    > button {
      padding: 8px;
      font-size: 9px;
      @include flexSet("center", "center");
    }

    .ant-input-number {
      width: 45px;
    }
  }

  &-group {
    margin: 0 10px;
    width: 80px;
  }
}
</style>
