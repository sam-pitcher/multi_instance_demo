explore: data {}

view: data {
  derived_table: {
    sql: SELECT current_date() AS date ;;
  }

  dimension: date {
    type: date
    convert_tz: no
  }

  dimension: new {
    type: yesno
  }

  dimension: sam {
    type: string
    # THIS IS TO PUSH TO PROD!!!!
  }

  dimension: environment {
    type: string
    sql: "{{_user_attributes['env']}}" ;;
  }
}
