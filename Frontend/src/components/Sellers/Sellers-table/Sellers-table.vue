<template>
  <div class="sellers-content-main-table">
    <table>
      <!-- SECTION table header -->

      <thead>
        <tr>
          <th>
            <div>
              <a-checkbox
                :indeterminate="indeterminate"
                :checked="checkAll"
                @change="onCheckAllChange"
              />
            </div>
          </th>
          <th v-for="column in columns" :key="column.dataIndex">
            <div>
              {{ column.title }}
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <!-- SECTION search row -->

        <tr>
          <td />

          <td v-for="column in columns.slice(0, 5)" :key="column.dataIndex">
            <div>
              <a-input
                :id="column.dataIndex"
                :value="input_value"
                @blur="updateSearchState"
                @keyup.enter="searchInput"
              />
            </div>
          </td>
          <!-- ANCHOR seller status -->
          <td>
            <div>
              <a-select
                :default-value="search_status"
                :value="search_status"
                style="width: 80px"
                @change="sellerStatusDropdown"
              >
                <a-select-option
                  v-for="stat in seller_status"
                  name="seller_status"
                  :key="stat.name"
                  :value="stat.seller_status_id"
                >
                  {{ stat.name }}
                </a-select-option>
              </a-select>
            </div>
          </td>
          <!-- ANCHOR email, phoneNumber -->
          <td v-for="column in columns.slice(6, 8)" :key="column.dataIndex">
            <div>
              <a-input
                :id="column.dataIndex"
                @blur="updateSearchState"
                @keyup.enter="searchInput"
              />
            </div>
          </td>

          <!-- ANCHOR seller attribute -->
          <td>
            <div>
              <a-select
                :default-value="search_attribute"
                :value="search_attribute"
                style="width: 100px"
                @change="sellerAttributeDropdown"
              >
                <a-select-option
                  v-for="attribute in seller_attribute_id"
                  name="seller_attribute_id"
                  :key="attribute.name"
                  :value="attribute.seller_attribute_id"
                >
                  {{ attribute.name }}
                </a-select-option>
              </a-select>
            </div>
          </td>

          <!-- ANCHOR calendar -->
          <td>
            <div>
              <a-date-picker
                placeholder="From"
                :value="search_start_time"
                @change="getStartTime"
              />
              <a-date-picker
                placeholder="to"
                :value="search_end_time"
                @change="getEndTime"
              />
            </div>
          </td>

          <!-- ANCHOR submit button -->
          <td>
            <div>
              <a-button type="primary" @click="submitSearch">
                <a-icon type="search" />
                <span>Search</span>
              </a-button>
              <a-button type="primary" @click="resetSearch">
                <a-icon type="close" />
                <span>Reset</span>
              </a-button>
            </div>
          </td>
        </tr>

        <!-- SECTION datarow -->

        <tr v-for="item in data" :key="item.id">
          <td>
            <div>
              <a-checkbox
                :id="item.id.toString()"
                class="listItems"
                @change="changeEachCheckBox"
              />
            </div>
          </td>

          <td>
            <div>
              {{ item.id }}
            </div>
          </td>

          <td>
            <div :id="item.id" @click="moveSellerDetails">
              {{ item.seller_id }}
            </div>
          </td>

          <template
            v-for="(val, name) in [
              item.eng_name,
              item.kor_name,
              item.owner_name,
              item.seller_status,
              item.phone_number,
              item.email,
              item.seller_attribute,
              item.created_at,
            ]"
          >
            <td :key="name">
              <div>
                {{ val }}
              </div>
            </td>
          </template>

          <td>
            <span>
              <a-button
                v-for="btn in item.seller_actions"
                :key="btn.id"
                :data-id="item.id"
                :data-btn="btn.id"
                :style="confirmBtnColor(+btn.id)"
                @click="updateAction"
              >
                {{ btn.name }}
              </a-button>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "SellersTable",

  components: {},

  props: {},

  data() {
    return {};
  },

  computed: {
    ...mapState({
      seller_attribute_id: ({ sellers }) => sellers.seller_attribute_id,
      seller_status: ({ sellers }) => sellers.seller_status,
      input_value: ({ sellers }) => sellers.input_value,
      select_value: ({ sellers }) => sellers.select_value,
      data: ({ sellers }) => sellers.data,
      columns: ({ sellers }) => sellers.columns,
      indeterminate: ({ sellers }) => sellers.indeterminate,
      checkAll: ({ sellers }) => sellers.checkAll,
      plainOptions: ({ sellers }) => sellers.plainOptions,
      checkedList: ({ sellers }) => sellers.checkedList,
      search_status: ({ sellers }) => sellers.search_input.seller_status_id,
      search_attribute: ({ sellers }) =>
        sellers.search_input.seller_attribute_id,
      search_start_time: ({ sellers }) => sellers.search_input.start_time,
      search_end_time: ({ sellers }) => sellers.search_input.end_time,
    }),
  },

  // SECTION Life cycle
  beforeUpdate() {
    this.getCheckboxId();
  },

  mounted() {
    this.initTableAction();
    // NOTE getSELLER_STATUS
    this.updateSellerStatusAction();
    // NOTE getSELLER_ATTRIBUTE_ID
    this.updateSellerAttributeAction();
  },

  methods: {
    // TODO move to seller detail
    moveSellerDetails(e) {
      const { id } = e.target;
      this.$router.push(`/main/seller/info/${id}`);
    },

    // SECTION btn styler
    confirmBtnColor(btn) {
      if (btn === 3 || btn === 6)
        return {
          background: `#f0ad4e`,
          border: "1px solid #eea236",
        };

      if (btn === 1 || btn === 4)
        return {
          background: `#5bc0de`,
          border: "1px solid #46b8da",
        };

      if (btn === 5 || btn === 2 || btn === 7)
        return {
          background: `#d9534f`,
          border: `1px solid #d43f3a`,
        };
    },

    // SECTION vuex
    ...mapActions("sellers", [
      "updateSellerStatusAction",
      "updateSellerAttributeAction",
      "initTableAction",
      "searchInput",
      "sellerStatusDropdown",
      "sellerAttributeDropdown",
      "getStartTime",
      "getEndTime",
      "updateSearchState",
      "submitSearch",
      "resetSearch",
      "updateAction",
      "changeEachCheckBox",
      "onCheckAllChange",
      "getCheckboxId",
      "downloadExcel",
    ]),
  },
};
</script>

<style src="./Sellers-table.scss" lang="scss" scoped />
