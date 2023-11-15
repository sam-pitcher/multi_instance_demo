explore: data {}

view: data {
  derived_table: {
    sql: SELECT current_date() AS date ;;
  }

  dimension: date {
    type: date
  }
}
