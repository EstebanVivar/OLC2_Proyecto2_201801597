export function obtenerFecha() {
    var fecha = new Date().toLocaleDateString("GT-gt");
    var hora = new Date().toLocaleTimeString("GT-gt");
    var date= fecha+" "+hora;
    return date;
}