explore: data {}

view: data {
  derived_table: {
    sql: SELECT current_date() AS date ;;
  }

  dimension: date {
    type: date
    convert_tz: no
  }

  dimension: environment {
    type: string
    sql: "{{_user_attributes['env']}}" ;;
  }
}
