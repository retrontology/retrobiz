const COLUMNS = ['#', 'Description', 'Hours', 'Rate', 'Total']
const DEC_REGEX = /^\d+(\.\d{1,2})?$/;

function ItemGrid(root) {
	this.init(root);
	return this;
}
ItemGrid.prototype = {
    init: function(root) {
        this.table = document.getElementById(root);
        this.create_header();
        this.add_row();
        let add_button = document.createElement("button");
        add_button.type="button";
        add_button.textContent = "Add an item";
        add_button.itemgrid = this;
        add_button.onclick = function(){this.itemgrid.add_row()};
        this.table.after(add_button);
    },
    create_header: function() {
        this.header = document.createElement("tr");
        for (const column of COLUMNS) {
            let cell = document.createElement("td");
            cell.textContent=column;
            this.header.appendChild(cell);
        }
        this.table.appendChild(this.header);
    },
    add_row: function() {
        let row = document.createElement("tr"); 
        let number_cell = document.createElement("td");
        let row_index = this.table.rows.length;
        number_cell.textContent = row_index;
        row.appendChild(number_cell);
        for (let i = 1; i < COLUMNS.length-1; i++) {
            let cell = document.createElement("td");
            let input = document.createElement("input");
            input.name = `item-${row_index}-${COLUMNS[i].toLowerCase()}`;
            input.itemgrid = this;
            if (i > 1)
                input.onchange = function(){this.itemgrid.calc_row(row_index)};
            cell.input = input;
            cell.appendChild(input);
            row.appendChild(cell);
        }
        let total_cell = document.createElement("td");
        row.appendChild(total_cell);
        let del_cell = document.createElement("td");
        let del_button = document.createElement("button");
        del_button.itemgrid = this;
        del_button.onclick = function(){this.itemgrid.del_row(row_index)};
        del_button.textContent="x";
        del_cell.appendChild(del_button);
        row.appendChild(del_cell);
        this.table.appendChild(row);
    },
    del_row: function(index) {
        this.table.rows[index].remove();
        this.reindex_rows(index);
    },
    reindex_rows: function(index=1) {
        for (let i = index; i < this.table.rows.length; i++) {
            let row = this.table.rows[i];
            row.cells[0].textContent = i;
            for (let j = 1; j < COLUMNS.length-1; j++) {
                input = row.cells[j].childNodes[0];
                name_parts = input.name.split('-');
                input.name = `item-${i}-${name_parts[2]}`;
            }
            row.cells[COLUMNS.length].childNodes[0].onclick = function(){this.table.del_row(i)};
        }
    },
    calc_row: function(index) {
        row = this.table.rows[index];
        hours = row.cells[2].input;
        rate = row.cells[3].input;
        if (DEC_REGEX.test(hours.value) && DEC_REGEX.test(rate.value))
            row.cells[4].textContent = hours.value*rate.value;
        else
            row.cells[4].textContent = "";
    },
}
