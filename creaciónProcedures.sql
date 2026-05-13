USE UDEMYTEST1;
GO

-- INSERTAR
CREATE PROCEDURE sp_InsertarEstudiante
    @IDEstudiante INT,
    @NombreEstudiante NVARCHAR(100),
    @ApellidoEstudiante NVARCHAR(100),
    @Email NVARCHAR(255),
    @Telefono NVARCHAR(20)
AS
BEGIN
    INSERT INTO Estudiantes
    VALUES(@IDEstudiante,@NombreEstudiante,@ApellidoEstudiante,@Email,@Telefono)
END
GO

-- CONSULTAR
CREATE PROCEDURE sp_ConsultarEstudiantes
AS
BEGIN
    SELECT * FROM Estudiantes
END
GO

-- ACTUALIZAR
CREATE PROCEDURE sp_ActualizarEstudiante
    @IDEstudiante INT,
    @NombreEstudiante NVARCHAR(100),
    @ApellidoEstudiante NVARCHAR(100),
    @Email NVARCHAR(255),
    @Telefono NVARCHAR(20)
AS
BEGIN
    UPDATE Estudiantes
    SET NombreEstudiante=@NombreEstudiante,
        ApellidoEstudiante=@ApellidoEstudiante,
        Email=@Email,
        Telefono=@Telefono
    WHERE IDEstudiante=@IDEstudiante
END
GO

-- ELIMINAR
CREATE PROCEDURE sp_EliminarEstudiante
    @IDEstudiante INT
AS
BEGIN
    DELETE FROM Estudiantes
    WHERE IDEstudiante=@IDEstudiante
END
GO