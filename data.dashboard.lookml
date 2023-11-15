- dashboard: data
  title: Data
  layout: newspaper
  preferred_viewer: dashboards-next
  description: ''
  preferred_slug: 1RcAbMlgBTSLGgv8bwjKYk
  elements:
  - name: This is content to move to the Production Instance
    type: text
    title_text: This is content to move to the Production Instance
    subtitle_text: ''
    body_text: ''
    row: 0
    col: 0
    width: 8
    height: 6
  - title: Today
    name: Today
    model: multi_instance_demo
    explore: data
    type: single_value
    fields: [data.date]
    fill_fields: [data.date]
    limit: 500
    custom_color_enabled: true
    show_single_value_title: true
    show_comparison: false
    comparison_type: value
    comparison_reverse_colors: false
    show_comparison_label: true
    enable_conditional_formatting: false
    conditional_formatting_include_totals: false
    conditional_formatting_include_nulls: false
    series_types: {}
    defaults_version: 1
    row: 0
    col: 8
    width: 16
    height: 6
