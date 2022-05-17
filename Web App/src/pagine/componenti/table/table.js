import './table.css'

const Table = ({ data, column }) => {
  return (
    <div className="cont">
    <table className="tabella">
      <thead className="row">
        <tr className="r">
          {column.map((item, index) => <TableHeadItem item={item} />)}
        </tr>
      </thead>
      <tbody className="row">
        {data.map((item, index) => <TableRow item={item} column={column} />)}
      </tbody>
    </table>
    </div>
  )
}

const TableHeadItem = ({ item }) => <th className="cella1">{item.heading}</th>

const TableRow = ({ item, column }) => (
  <tr class="r">
    {column.map((columnItem, index) => {
      return <td className="cella">{item[`${columnItem.value}`]}</td>
    })}
  </tr>
)


export default Table